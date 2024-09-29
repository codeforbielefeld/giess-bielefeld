<button
	{...$$props}
	on:click|stopPropagation
	class={`rounded-full px-4 py-2 ${$$props.class}`}
	on:click>{$$props.label}</button
>
