<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

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
	<div class="container mx-auto z-[1100] bg-white p-4 rounded-t-xl max-h-3/4 overflow-y-auto">
		<div class="flex flex-row items-center justify-between">
			<div>
				<h1 class="text-2xl font-bold">{title}</h1>
			</div>
			{#if closeable}
				<button class="shrink" on:click={close}>
					<img src="/cross.svg" />
				</button>
			{/if}
		</div>
		<slot />
	</div>
{/if}
<!-- Card END -->
