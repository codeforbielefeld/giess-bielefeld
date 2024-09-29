<script>
	import BaseButton from './BaseButton.svelte';
</script>

<BaseButton
	{...$$props}
	on:click
	class={`${$$props.class} border-2 border-black text-black`}
	label={$$props.label}
/>
