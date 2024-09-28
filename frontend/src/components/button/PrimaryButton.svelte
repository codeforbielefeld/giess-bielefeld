<script>
	import BaseButton from './BaseButton.svelte';
</script>

<BaseButton
	{...$$props}
	{...$$restProps}
	class={`${$$props.class} bg-green-500 hover:bg-green-300 text-black`}
	label={$$props.label}
/>
