<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import Heading from '../typography/Heading.svelte';

	export let title;
	export let closeable: boolean | undefined = true;
	export let open: boolean = true;

	$: open, closeable;

	onMount(() => {
		if (closeable === undefined) {
			closeable = true;
		}
	});

	const close = () => {
		open = false;
		goto('/');
	};
</script>

<!-- Card START -->
{#if open}
	<div
		id="card"
		class="container mx-auto z-[1100] bg-white px-4 pt-4 rounded-t-xl h-[80vh] max-h-[80vh]"
		on:click|stopPropagation
		role="button"
		tabindex="0"
		on:keydown={(e) => {
			if (e.key !== 'Enter' && e.key !== ' ') return;
			e.preventDefault();
			e.target.click();
		}}
	>
		<div id="card-content" class="flex flex-col h-full">
			<!-- Navigation -->
			<div class="flex flex-row items-center justify-between shrink">
				{#if closeable}
					<button class="shrink" on:click={close}>
						<img src="/cross.svg" alt="" />
					</button>
				{/if}
			</div>
			<!-- Navigation END -->

			<slot name="navigation" />

			<!-- Card Content -->
			<div class="overflow-y-auto grow">
				<slot />
			</div>
			<!-- Card Content END -->
		</div>
	</div>
{/if}
<!-- Card END -->
