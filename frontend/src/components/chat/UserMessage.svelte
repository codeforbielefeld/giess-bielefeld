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
	<div class="w-11/12">
		<div class="p-3 text-black rounded-xl bg-message-user box-border">
			{message.text}
		</div>
	</div>
	<div class="w-1/12 pt-2">
		<img src="/userIcon.svg" alt="Bot" class="w-8 h-8" />	
	</div>
</div>