<script>
	import BaseButton from './BaseButton.svelte';
</script>

<a
	href={$$props.href}
	{...$$props}
	{...$$restProps}
	class={`${$$props.class} rounded-full px-4 py-2 border-2 border-green-500 text-black text-center`}
>
	{$$props.label}
</a>

<a href={$$props.hres}>
<BaseButton
	on:click
	{...$$props}
	{...$$restProps}
	class={` border-2 border-green-500 text-black text-center ${$$props.class}` }
	label={$$props.label}
/>
</a>