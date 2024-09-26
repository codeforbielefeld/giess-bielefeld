<script>
    export let water_history;


</script>

<img src="/wasserSäule.svg"/>


<svg>
    {#each water_history as water}
        <rect
            x="0"
            y="0"
            fill="blue"
            width="20"
            height="{water.amount}"/>
            HALLO
    {/each}
</svg>
