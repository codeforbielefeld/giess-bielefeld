<script lang="ts">
	import Card from "../../components/card/Card.svelte";
	import Heading from "../../components/typography/Heading.svelte";
    import BaseButton from "../../components/button/BaseButton.svelte";
	import DefaultButton from "../../components/button/DefaultButton.svelte";
	import LinkButton from "../../components/button/LinkButton.svelte";
	import PrimaryButton from "../../components/button/PrimaryButton.svelte";
	import SecondaryButton from "../../components/button/SecondaryButton.svelte";

</script>

<Card title={"search"} open={true}>
	<Heading level={1}>Bäume filtern</Heading>
	<div>Standort filtern</div>
	<div>Nach Alter filtern</div>
	<div>Nach Wasserbedarf filtern</div>
	<div>
		Button Testing
        <Heading level={2}>Deine adoptierten Bäume</Heading>
        <BaseButton label={"Base"}/>
        <LinkButton label={"link"}/>
        <DefaultButton label={"default"} icon_src={"/tree.svg"} icon_alt={"Baum"}/>
        <PrimaryButton label={"primary"}/>
        <DefaultButton label={"default"} icon_src={"/tree.svg"} icon_alt={"Baum"}/>
        <LinkButton label={"link"}/>
        <SecondaryButton label={"secondary"}/>
   
    </div>
</Card>