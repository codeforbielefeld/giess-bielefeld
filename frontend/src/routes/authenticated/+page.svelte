<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import Card from '../../components/card/Card.svelte';
	import { supabase } from '../../supabase';

	let userEmail: string | undefined = '';

	onMount(async () => {
		const { data } = await supabase.auth.getUser();
		userEmail = data.user?.email;
	});

	const handleLogout = () => {
		supabase.auth.signOut().then(() => {
			goto('/');
		});
	};
</script>

<Card title="Authenticated Page" closeable={false}>
	<p>Deine Mail-Adresse: {userEmail}</p>
	<button class="px-4 py-2 border border-red-500 rounded-full" on:click={handleLogout}
		>Logout</button
	>
</Card>
