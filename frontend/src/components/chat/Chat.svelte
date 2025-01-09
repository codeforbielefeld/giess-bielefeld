<script lang="ts">
	import BotMessage from './BotMessage.svelte';
	import Message from './Message.svelte';
	import UserMessage from './UserMessage.svelte';

	interface Message {
		text: string;
		label: string;
		type: string;
		sender: string;
		source?: string;
		clickable?: boolean;
	}

	let messages: Array<Message> = [];

	let newMessage: string = '';
	let chatAvailable: boolean = true;

	messages = [
		{
			text: 'Hallo! Ich bin eine Winter Linde. Wie sehe ich aus? lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
			label: 'Willkommen',
			type: 'text',
			sender: 'bot',
			ai: true
		},
		{
			text: 'prächtig',
			label: 'gut',
			type: 'choice',
			sender: 'bot',
			clickable: true
		},
		{
			text: 'durstig',
			label: 'durst',
			type: 'choice',
			sender: 'bot',
			clickable: true
		},
		{
			text: 'unklar',
			label: 'unklar',
			type: 'choice',
			sender: 'bot',
			clickable: true
		},
		{
			text: 'Du bist sehr schön',
			label: 'Antwort',
			type: 'text',
			sender: 'user',
			clickable: true
		}
	];

	function sendMessage(text: string, label: string) {
		// Implementation for sending message
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter' && newMessage !== '') {
			sendMessage(newMessage, newMessage);
		}
	}
</script>

<div id="chat-container" class="flex flex-col">
	<div class="grow">
		<div class="sticky top-0 min-h-12 h-12 w-100 bg-gradient-to-b from-white z-[9999999]"></div>
		<div class="flex flex-col h-full overflow-y-auto gap-y-1">
			{#each messages as message}
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<Message {message} />
				<!-- <div>
				{#if type === 'choice'}
				<button
				on:click={(e) => {
					clickable && sendMessage(text, label);
					}}
					>
					{#if sender === 'bot' && text === 'Gesundheits-Check'}
					🌡️
					{:else if sender === 'bot' && text === 'Wasserbedarf'}
					💧
					{:else if sender === 'bot' && text === 'Bauminfos'}
					🌳
					{/if}
					{text}
					</button>
					{:else if type === 'text'}
					<BotMessage {text} />
					{:else if type === 'small'}
					<UserMessage {text} />
					{:else if type === 'visual'}
					<div>
						<img src={source} alt="grafik Regenmenge" />
						</div>
						{/if}
						</div> -->
			{/each}
		</div>
	</div>

	<div class="shrink bottom-0 sticky pt-2 bg-white border-t border-t-gray-500" >
		<div class="flex flex-row gap-1.5">
			<input class="grow bg-green-500 rounded-full py-1 px-3 placeholder:text-neutral-500  placeholder:italic"
				disabled={!chatAvailable}
				bind:value={newMessage}
				placeholder={chatAvailable ? '' : 'Chat beendet.'}
				on:keydown={handleKeydown}
			/>
			<button class="shrink w-1/12"
				disabled={!chatAvailable}
				on:click={(e) => {
					if (newMessage !== '') {
						sendMessage(newMessage, newMessage);
					}
				}}
			>
				<img src="/sendIcon.svg" class="w-8 h-8" alt="senden">
			</button>
		</div>
	</div>
</div>

<style>
</style>
