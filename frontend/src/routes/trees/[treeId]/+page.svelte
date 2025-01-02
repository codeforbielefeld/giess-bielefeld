<!--Seite für 1 individuellen Baum :) -->
<script lang="ts">
	import { Accordion, AccordionItem } from 'svelte-collapsible';
	import WaterColumn from '../../../components/WaterColumn.svelte';
	import Chat from '../../../components/chat/Chat.svelte';
	import Card from '../../../components/card/Card.svelte';
	export let data;

	export let activeTabIndex: number = 0;

	function handleTabChange(tab: number) {
		activeTabIndex = tab;
	}

	$: showInfo = true;
	$: showChat = false;

	$: buttonLabels = ['Infos', 'Chat'];

	let testreeprops = {
		pitID: '00008100:00c0fbd5',
		Standort_N: 1,
		Zusatz: null,
		laufende_n: '1',
		gefaellt: 0,
		Stammdurch: 80.0,
		Kronendurc: 12.0,
		Baumhoehe_: 21.0,
		Stammumfan: 251.33,
		Baumgruppe: 0,
		Bezirk_Nr: '11',
		Bezirk_Bez: 'WEST - BUERGERPARK',
		Objekt_Nr: '001',
		Objekt_Bez: 'GA BÃ¼rgerpark',
		Baumart_bo: 'Quercus robur',
		Baumart_de: 'Stiel-Eiche',
		Baumart_ku: 'q r',
		PflE_Art_N: '1270',
		PflE_Art_B: 'Einzelbaum',
		Stammradiu: 40.0,
		Kronenradi: 6.0,
		geometry: { type: 'Point', coordinates: [8.511457515202823, 52.026940411111674] },
		waterdata: [
			{
				source: 'Dir',
				amount: 20
			},
			{
				source: 'Peter',
				amount: 10
			},
			{
				label: 'Stadt',
				amount: 30
			},
			{
				label: 'Regen',
				amount: 30
			}
		]
	};

	const {
		Baumart_de: art_de,
		Stammdurch: durchmesser_stamm,
		Kronendurc: durchmesser_krone,
		Baumhoehe_: hoehe,
		Stammumfan: umfang_stamm,
		waterdata: water_history
	} = testreeprops;
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
			{:else}
				<Chat />
			{/if}
		</div>
	</div>
</Card>
