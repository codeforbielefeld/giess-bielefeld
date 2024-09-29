<script lang="ts">
	import { onMount } from 'svelte';
	import { supabase } from '../../../supabase';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';
	import Dialog from '../../../components/dialog/Dialog.svelte';
	import PrimaryButton from '../../../components/button/PrimaryButton.svelte';
	import SecondaryButton from '../../../components/button/SecondaryButton.svelte';
	import EmailField from '../../../components/input/EmailField.svelte';
	import PasswordField from '../../../components/input/PasswordField.svelte';
	import LinkButton from '../../../components/button/LinkButton.svelte';

	let email: string = 'daniel@barooney.com';
	let password: string = '12345678';
	let passwordConfirmation: string = '12345678';
	let emailErrorCode: string = '';
	let passwordErrorCode: string = '';
	$: email, password, passwordConfirmation, emailErrorCode, passwordErrorCode;

	let loading: boolean = false;

	onMount(() => {
		const { data } = supabase.auth.onAuthStateChange((event, session) => {
			console.log(event, session);

			if (event === 'INITIAL_SESSION') {
				// handle initial session
			} else if (event === 'SIGNED_IN') {
				// handle sign in event
			} else if (event === 'SIGNED_OUT') {
				// handle sign out event
			} else if (event === 'PASSWORD_RECOVERY') {
				// handle password recovery event
			} else if (event === 'TOKEN_REFRESHED') {
				// handle token refreshed event
			} else if (event === 'USER_UPDATED') {
				// handle user updated event
			}
		});

		// call unsubscribe to remove the callback
		data.subscription.unsubscribe();
	});

	const handleRegistration = async (e: any) => {
		e.preventDefault();

		if (password !== passwordConfirmation) {
			passwordErrorCode = 'Die Passwörter stimmen nicht überein!';
			return;
		}

		loading = true;
		supabase.auth
			.signUp({
				email,
				password
			})
			.then(({ data, error }) => {
				console.log(data, error);
				if (error) {
					switch (error.code) {
						case 'user_already_exists':
							emailErrorCode = 'Es ist ein Fehler bei der Registrierung aufgetreten.';
							break;
						case 'validation_failed':
							emailErrorCode = 'Die eingegebene E-Mail-Adresse ist ungültig.';
							break;
						case 'weak_password':
							passwordErrorCode = 'Das Passwort ist zu schwach.';
							break;
						default:
							emailErrorCode = error.code || 'unknown error';
							break;
					}
				} else {
					goto('/authenticated');
				}
			});
	};
</script>

<Dialog title="Registrierung">
	<form class="flex flex-col gap-y-4">
		<div class="flex flex-col gap-y-2">
			<EmailField
				id="email"
				label="E-Mail:"
				inputClass="w-full"
				placeholder="jdoe@example.com"
				error={emailErrorCode}
				bind:value={email}
			/>
			<PasswordField
				id="password"
				label="Passwort:"
				inputClass="w-full"
				placeholder="Passwort"
				error={passwordErrorCode}
				bind:value={password}
			/>
			<PasswordField
				id="password_confirmation"
				label="Passwort (Wiederholung):"
				inputClass="w-full"
				placeholder="Passwort"
				error={passwordErrorCode}
				bind:value={passwordConfirmation}
			/>
		</div>
		<div class="flex flex-col gap-y-2">
			<PrimaryButton
				type="submit"
				label="Registrieren"
				class="w-full"
				onClick={handleRegistration}
			/>
			<LinkButton href="/login" label="Anmelden" class="w-full" />
		</div>
	</form>
</Dialog>
