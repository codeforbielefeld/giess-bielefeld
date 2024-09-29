<script lang="ts">
    export let water;
    import {scaleLinear, scaleOrdinal} from "d3-scale";
	import { scale } from "svelte/transition";

    console.log("water", water)
    let margin = 10;
    let colWidth = 30;
    let colHeight = 300;
    let chartWidth;
    const waterSum = water.reduce((sum: any, item: { amount: any; }) => sum + item.amount, 0);
 
    $: heightScale = scaleLinear()
			.domain([0, waterSum])
			.range([0, colHeight])

    const nameScale = scaleOrdinal<string, string>()
            .domain(["rain", "city", "users", "thisUser", "missing"])
            .range(["Regen", "Stadt", "BaumBIEs", "Du", "fehlen"]);

    const colorScale = scaleOrdinal<string, string>()
            .domain(["rain", "city", "users", "thisUser", "missing"])
            .range(["#7C99B2", "#5E7386", "#458E72", "#51AF8B", "#E20C151A"]);


    // Array to store the calculated heights and positions
    interface StackedElement {
        source: string;
        amount: number;
        height: number;
        y: number;
    }

    // Calculate heights and positions for the stacked chart
    $: stackedData = water.map((d: { source: string; amount: number }, index: number, arr: StackedElement[]) => {
        const height = heightScale(d.amount);
        
        // Calculate the cumulative height of all previous elements for the y position
        const y = index === 0 ? 0 : arr.slice(0, index).reduce((sum, prev) => sum + heightScale(prev.amount), 0);
        
        return {
            source: d.source,
            color: colorScale(d.source),
            amount: d.amount,
            height: height,
            y: y
        };
        });



</script>

<img src="/wasserSäule.svg"/>

<div bind:clientWidth={chartWidth}>
    <p>Water History:</p>
    <svg width={colWidth + margin} height={colHeight}>
        {#each stackedData as d}
            <rect
                x="10"
                y="{d.y}"
                fill="{d.color}"
                width="{colWidth}"
                height="{d.height}"
                rx="15"/>
        {/each}
    </svg>
</div>
