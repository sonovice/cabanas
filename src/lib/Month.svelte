<script lang="ts">
    export let year: number;
    export let month: number;
    export let data: object;
    export let max: number = 3;

    import calendarize from "calendarize";
    import colormap from "colormap";

    let colors = colormap({
        colormap: "hot",
        nshades: max + 2,
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
</script>

<div>
    <div
        class="bg-cyan-700 p-2 rounded-t-lg text-white font-medium flex items-center pl-2"
    >
        {months[month - 1]}
    </div>
    <div class="bg-white rounded-b-lg overflow-hidden">
        <table class="w-full table-fixed">
            <tr>
                {#each weekdays as weekday}
                    <th class="w-1/[7] text-center py-2">{weekday}</th>
                {/each}
            </tr>
            {#each view as week}
                <tr>
                    {#each week as day}
                        {#if day > 0}
                            <td
                                class="text-right text-white h-12 text-xs align-top pr-2 pt-1"
                                class:text-white={data[day] != undefined &&
                                    data[day].length > max / 2}
                                title={data[day] != undefined
                                    ? `${data[day].length} MAC(s):\n${data[
                                          day
                                      ].join("\n")}`
                                    : ""}
                                style="background-color: {data[day] != undefined
                                    ? colors[Math.min(max, data[day].length)]
                                    : 0}"
                                >{day}
                            </td>
                        {:else}
                            <td class="bg-gray-200"/>
                        {/if}
                    {/each}
                </tr>
            {/each}
        </table>
    </div>
</div>
