<script>
	import BaseButton from './BaseButton.svelte';
</script>

<BaseButton
	{...$$props}
	{...$$restProps}
	class={`${$$props.class} border-2 border-green-500 text-black`}
	label={$$props.label}
/>
