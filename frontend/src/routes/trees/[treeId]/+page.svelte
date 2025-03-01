<!--Seite für 1 individuellen Baum :) -->
<script lang="ts">
	import { Accordion, AccordionItem } from 'svelte-collapsible';
	import WaterColumn from '../../../components/WaterColumn.svelte';
	import Chat from '../../../components/chat/Chat.svelte';
	import Card from '../../../components/card/Card.svelte';

	import AdoptTree from '../../../features/adoption/AdoptTree.svelte';
	import { supabase } from '../../../supabase';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import type { Tree } from '../../../types/Tree';

	export let activeTabIndex: number = 0;

	function handleTabChange(tab: number) {
		activeTabIndex = tab;
	}

	$: showInfo = true;
	$: showChat = false;

	$: buttonLabels = ['Infos', 'Chat'];


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

{#if tree}
<Card title={`${tree.tree_type_german}, ALTER`} open={true}>
	<!-- svelte-ignore a11y-no-noninteractive-element-to-interactive-role -->

	<div slot="navigation">
		<nav
			id="single-tree-navigation"
			class="flex flex-col justify-center px-3 py-2 text-base font-medium text-center bg-green-600 bg-opacity-60 rounded-md shadow-sm whitespace-nowrap"
			role="tablist"
			aria-label="Content sections"
		>
			<section class="relative flex items-center justify-between w-full">
				<div
					class={`absolute transition-transform ${activeTabIndex === 0 ? 'translate-x-0' : 'translate-x-full'} z-0 bg-white rounded h-[100%] shadow-[0px_1px_4px_rgba(0,0,0,0.15)] w-[50%]`}
				/>

				<button
					role="tab"
					aria-selected={activeTabIndex === 0}
					aria-controls="info-panel"
					class="flex-1 py-2 shrink gap-2.5 self-stretch my-auto ${showInfo
						? 'text-zinc-600'
						: 'text-neutral-500'} z-10"
					on:click={() => handleTabChange(0)}
					tabindex="0"
				>
					Infos
				</button>
				<button
					role="tab"
					aria-selected={activeTabIndex === 1}
					aria-controls="chat-panel"
					class="flex-1 py-2 shrink gap-2.5 self-stretch my-auto ${showChat
						? 'text-zinc-600'
						: 'text-neutral-500'} z-10"
					on:click={() => handleTabChange(1)}
					tabindex="0"
				>
					Chat
				</button>
			</section>
		</nav>
	</div>

	<div id="single-tree-content" class="flex flex-col">
		<div>
			{#if activeTabIndex === 0}
				<Accordion>
					<AccordionItem key="a">
						<div slot="header">
							<div class="inline-flex flex-row items-start gap-2.5">
							<p class="text-black font-cera-bielefeld text-base font-bold leading-normal">
							Über Mich
							</p>
							<button class="translate-y-1.5"><img src="/plusButton.svg" alt="Plusbutton" /></button>
							</div>
						</div>
						<p slot="body">
							Höhe: {tree.height}<br />
							Kronendurchmesser: {tree.crown_diameter}<br />
							Stammdurchmesser: {tree.trunk_diameter}
						</p>
					</AccordionItem>
					<AccordionItem>
						<h2 slot="header">Wasserbedarf</h2>
						<p slot="body"><WaterColumn/></p>
					</AccordionItem>
					<AccordionItem>
						<h2 slot="header">Wer wann geossen hat</h2>
						<p slot="body">Hier werden die letzten 10 Gießungen angezeigt</p>
					</AccordionItem>
				</Accordion>

      		<AdoptTree {tree} />
			{:else}
				<Chat />
			{/if}
		</div>
	</div>

</Card>
{/if}
