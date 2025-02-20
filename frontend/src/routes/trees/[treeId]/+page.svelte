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

	export let data;

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

<Card title={`${art_de}, ALTER`} open={true}>
	<!-- svelte-ignore a11y-no-noninteractive-element-to-interactive-role -->

	<div slot="navigation">
		<nav
			id="single-tree-navigation"
			class="flex flex-col justify-center px-3 py-2 text-base font-medium text-center bg-green-300 rounded-md shadow-sm whitespace-nowrap"
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
						<h2 slot="header">
							Über Mich
							<button><img src="/plusButton.svg" alt="Plusbutton" /></button>
						</h2>
						<p slot="body">
							Höhe: {hoehe}<br />
							Kronendurchmesser: {durchmesser_krone}<br />
							Stammdurchmesser: {durchmesser_stamm}
						</p>
					</AccordionItem>
				</Accordion>
				<WaterColumn />
      {#if tree}
      		<AdoptTree {tree} />
      {/if}
			{:else}
				<Chat />
			{/if}
		</div>
	</div>

</Card>
