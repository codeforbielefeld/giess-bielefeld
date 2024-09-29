<!--Seite für 1 individuellen Baum :) -->
<script lang="ts">
	import { Accordion, AccordionItem } from 'svelte-collapsible';
	import WaterColumn from '../../../components/WaterColumn.svelte';
	import Card from '../../../components/card/Card.svelte';
	import AdoptTree from '../../../features/adoption/AdoptTree.svelte';
	import { supabase } from '../../../supabase';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import type { Tree } from '../../../types/Tree';

	export let tree: Tree;

	$: tree;

	onMount(async () => {
		const { data, error } = await supabase
			.from('trees')
			.select()
			.eq('uuid', $page.params.treeId)
			.maybeSingle();
		tree = data;
	});
</script>

<Card title={`${tree?.tree_type_german}, ALTER`} open={true}>
	<Accordion>
		<AccordionItem key="a">
			<h2 slot="header">
				Über diesen Baum
				<button><img src="/plusButton.svg" /></button>
			</h2>
			<!-- <p slot="body">
				Höhe: {hoehe}<br />
				Kronendurchmesser: {durchmesser_krone}<br />
				Stammdurchmesser: {durchmesser_stamm}
			</p> -->
		</AccordionItem>
	</Accordion>
	<!-- <WaterColumn {water_history} /> -->
	{#if tree}
		<AdoptTree {tree} />
	{/if}
</Card>
