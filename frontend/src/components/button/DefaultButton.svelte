<script>
	import BaseButton from './BaseButton.svelte';
</script>

<BaseButton
	{...$$props}
	class={`${$$props.class} border-2 border-black text-black`}
	label={$$props.label}
/>
