<script lang="ts">
	import { onMount } from 'svelte';
	import PrimaryButton from '../../components/button/PrimaryButton.svelte';
	import Heading from '../../components/typography/Heading.svelte';
	import Typography from '../../components/typography/Typography.svelte';
	import { supabase } from '../../supabase';
	import type { Tree } from '../../types/Tree';

	export let tree: Tree;

	let errorMessage: string = '';
	let successMessage: string = '';
	let adopted = false;
	let label = '';
	$: tree, adopted;

	onMount(async () => {
		const user = await supabase.auth.getUser();
		const userId = user?.data?.user?.id;
		const treeId = tree.uuid;

		const adoptedData = await supabase
			.from('adoptions')
			.select('*')
			.eq('tree_uuid', treeId)
			.eq('user_uuid', userId);
		adopted = adoptedData.data?.length !== 0;
		label = adopted ? 'Du hast diesen Baum bereits adoptiert' : 'Adoptiere diesen Baum';
	});

	const handleAdoptTree = async () => {
		let { data, error }: any = await supabase.auth.getUser();
		if (error) {
			errorMessage = error;
			return;
		}
		({ data, error } = await supabase
			.from('adoptions')
			.insert({ tree_uuid: tree.uuid, user_uuid: data?.user?.id })
			.select());
		if (error) {
			errorMessage =
				'Beim Adoptieren des Baumes ist ein Fehler aufgetreten. Hast du ihn vielleicht bereits adoptiert?';
			successMessage = '';
			return;
		}

		adopted = true;
		successMessage = 'Du hast diesen Baum erfolgreich adoptiert!';
		errorMessage = '';
	};
</script>

{#if tree}
	<div>
		<Heading level={2}>Baum adoptieren</Heading>
		<Typography class="mb-4"
			>Mit einer Adoption dieses Baums zeigst du deine Verbundenheit mit diesem Baum und der Stadt,
			denn Bäume helfen allen Menschen in deiner Stadt, ein lebenswerteres und gesundes Leben zu
			leben.</Typography
		>
		<PrimaryButton disabled={adopted} {label} on:click={handleAdoptTree} />
		<p class="text-orange-500">{errorMessage}</p>
		<p class="text-green-500">{successMessage}</p>
	</div>
{/if}
