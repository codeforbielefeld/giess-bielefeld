<!--Seite für 1 individuellen Baum :) -->
<script lang="ts">
	export let data;
	console.log(data.treeId);

</script>

<div class="mx-auto">
<div class="container">

	<div class="absolute w-full h-[85%] bottom-0 self-center justify-center z-[700] bg-white">
		<p>Hallo Baum {data.treeId}</p>
	</div>

</div>
</div>