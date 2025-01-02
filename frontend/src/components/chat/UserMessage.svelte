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

<div class="user-message">User: {message.text}</div>
