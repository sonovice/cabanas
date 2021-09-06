<script lang="ts">
    export let year: number;
    export let month: number;
    export let data: object;
    export let max: number = 3;

    import calendarize from "calendarize";
    import colormap from "colormap";

    const nShades = Math.max(9, Math.ceil(max * 1.5));

    let colors = colormap({
        colormap: "magma",
        nshades: nShades,
        format: "hex",
        alpha: 1,
    }).reverse();

    const weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    const view = calendarize(`${year}-${month}`, 1);
    let bgColors = Array(32).fill("#ffffff");
    let textColors = Array(32).fill("text-black");
    for (let day in data) {
        const numMacs = Math.min(max, data[day].length);
        bgColors[day] = colors[numMacs];
        textColors[day] = numMacs < nShades / 2 ? "text-black" : "text-white";
    }
</script>

<div>
    <div
        class="flex items-center justify-center p-2 tracking-wide text-white uppercase bg-teal-800 rounded-t-lg"
    >
        {months[month - 1]}
        {year}
    </div>
    <div class="overflow-hidden bg-white rounded-b-lg">
        <table class="w-full bg-white table-fixed">
            <tr class="bg-true-gray-800">
                {#each weekdays as weekday}
                    <td
                        class="w-1/[7] text-center text-sm font-medium py-2 text-white"
                        >{weekday}</td
                    >
                {/each}
            </tr>
            {#each view as week}
                <tr>
                    {#each week as day}
                        {#if day > 0}
                            <td
                                class="h-12 text-2xl font-black text-center {textColors[day]} text-opacity-30"
                                title={
                                    data[day] != undefined
                                    ? `${data[day].length} MAC(s):\n${data[day].join("\n")}`
                                    : "No Devices connected."
                                }
                                style="background-color: {bgColors[day]}"
                                >{day}
                            </td>
                        {:else}
                            <td class="bg-true-gray-300" />
                        {/if}
                    {/each}
                </tr>
            {/each}
        </table>
    </div>
</div>