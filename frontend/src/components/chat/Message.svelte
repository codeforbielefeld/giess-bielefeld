<script lang="ts">
	import BotMessage from './BotMessage.svelte';
	import UserMessage from './UserMessage.svelte';

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

<div
	class={`message flex flex-row w-full ${message.sender === 'bot' ? 'justify-start' : 'justify-end'} mb-2`}
>
	{#if message.sender === 'bot'}
		<BotMessage {message} />
	{:else if message.sender === 'user'}
		<UserMessage {message} />
	{/if}
</div>
