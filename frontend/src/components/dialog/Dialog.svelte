<script lang="ts">
	import { onMount } from 'svelte';
	import Heading from '../typography/Heading.svelte';
	import { goto } from '$app/navigation';

	export let title: string = '';

	const onClickBackdrop = (e: any) => {
		goto('/');
	};
</script>

<!-- Backdrop START -->
<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div
	class="fixed top-0 left-0 w-full h-full z-[1100] bg-gray-700 bg-opacity-50"
	on:click={onClickBackdrop}
>
	<div class="z-[1200] flex items-center justify-center w-full h-full" on:click|stopPropagation>
		<!-- Box START -->
		<div class="px-8 py-4 bg-white w-96 rounded-xl">
			<Heading level={1}>{title}</Heading>
			<slot />
		</div>
		<!-- Box END -->
	</div>
</div>
<!-- Backdrop END -->
