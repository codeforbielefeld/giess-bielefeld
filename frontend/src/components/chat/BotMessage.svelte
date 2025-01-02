<script lang="ts">
	interface Message {
		text: string;
		label: string;
		type: string;
		sender: string;
		source?: string;
		clickable?: boolean;
		ai?: boolean;
	}

	export let message: Message;
</script>

<div class="flex flex-row w-full bot-message">
	<div class="flex justify-center w-1/12 pt-2 align-center">
		{#if message.ai}
			<img src="/tree-ai.svg" alt="Bot" class="w-6 h-6" />
		{:else}
			<img src="/tree.svg" alt="Bot" class="w-6 h-6" />
		{/if}
	</div>
	<div class="w-11/12">
		<div class="p-2 text-black rounded-xl bg-neutral-300">
			{message.text}
		</div>
	</div>
</div>
