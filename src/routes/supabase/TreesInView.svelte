<script lang="ts">
	import { supabase } from '../../supabase';

	let trees;
	$: trees = [];

	let min_lat = 52.026731;
	let min_long = 8.5297468;

	let max_lat = 52.0195512;
	let max_long = 8.5474625;

	const getTreesInView = () => {
		supabase.rpc('trees_in_view', {
			min_lat, min_long, max_lat, max_long
		}).then(({ data, error }) => {
			if (error) {
				console.error(error);
			} else {
				trees = data;
			}
		});
	};
</script>

<div>
	<div class="flex row space-x-4">
		<div>
			<label for="min-lat-input" >Längengrad links:</label>
			<input id="min-lat-input" type="number" value={min_lat} class="border border-black rounded-sm" />
		</div>

		<div>
			<label for="min-long-input">Breitengrad oben:</label>
			<input id="min-long-input" type="number" value={min_long} class="border border-black rounded-sm" />
		</div>

		<div>
			<label for="max-lat-input" >Längengrad rechts:</label>
			<input id="max-lat-input" type="number" value={max_lat} class="border border-black rounded-sm" />
		</div>

		<div>
			<label for="max-long-input">Breitengrad unten:</label>
			<input id="max-long-input" type="number" value={max_long} class="border border-black rounded-sm" />
		</div>

		<button on:click={()=>getTreesInView()}>Bäume laden</button>

	</div>

	<div>Bäume in der Nähe:</div>
	<ul class="list-disc max-h-64 overflow-y-scroll">
		{#each trees as tree}
			<li>
				{tree.tree_type_german}
			</li>
		{/each}
	</ul>
</div>