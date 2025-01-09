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

<div class="flex gap-1.5 flex-row w-full bot-message">
	<div class="w-1/12 pt-2 ">
			<img src="/tree.svg" alt="Bot" class="w-8 h-8" />	
	</div>
	<div class="w-11/12">
		<div class="p-3 text-black rounded-xl bg-message-bot box-border">
			{message.text}
			{#if message.ai}
			<span class="text-gray-400 text-xs float-right inline-block mt-2">KI-generiert</span>
			<div class="clear-both"></div>
			{/if}
		</div>
	</div>
</div>
