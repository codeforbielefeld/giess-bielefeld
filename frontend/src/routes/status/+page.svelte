<script lang="ts">
	import DefaultButton from "../../components/button/DefaultButton.svelte";
    import Card from "../../components/card/Card.svelte";
    import Heading from "../../components/typography/Heading.svelte";

    import { onMount } from "svelte";
    import { supabase } from "../../supabase";

    async function getUserData() {
        const user = await supabase.auth.getUser();
        return user;
    }

    $: user = {"data":{"user":{}}};
    $: user_id = "";
    $: adopted_ids = [];

    onMount(async () => {
        user = await getUserData();
        user_id = user.data.user.id;
        const { data, error } = await supabase
            .from('adoptions')
            .select()
            .eq('user_uuid', user_id);
        adopted_ids = data?.map(tree => tree.tree_uuid);
    });



    $:console.log("user id:", user.data.user.id);

    $:console.log("adopted ids:", adopted_ids)
</script>


<Card title={"search"} open={true}>
	<Heading level={1}>Dein Status</Heading>
	<div>
        <Heading level={2}>Gießfortschritt</Heading>
    </div>
    <div>
        <Heading level={2}>Deine adoptierten Bäume</Heading>
        {#each adopted_ids as id}
        <DefaultButton label={id} icon_src={"/tree.svg"} icon_alt={"Baum"}/>
        {/each}
    </div>
    <div>
        <Heading level={2}>Bäume in deiner Nähe</Heading>
    </div>
</Card>