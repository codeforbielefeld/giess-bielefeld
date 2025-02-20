<script lang="ts">
	interface Message {
		text: string;
		label: string;
		type: string;
		sender: string;
		source?: string;
		clickable?: boolean;
	}

	export let message: Message;
</script>

<div class="flex gap-1.5 flex-row w-full flex-end">
	<div class="flex flex-grow">
		<div class="p-3 text-black rounded-xl bg-message-user box-border w-full">
			{message.text}
		</div>
	</div>
	<div class="pt-2">
		<img src="/userIcon.svg" alt="Bot" class="min-w-8 min-h-8" />	
	</div>
</div>