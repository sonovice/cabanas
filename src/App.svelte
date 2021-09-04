<script lang="ts">
  import Month from "./lib/Month.svelte";
  let data: Object = {};
  let numColors = 0;

  fetch("https://raw.githubusercontent.com/sonovice/cabanas/main/data.json")
    .then((response) => response.json())
    .then((response) => {
      data = response;

      for (let year in data) {
        for (let month in data[year]) {
          for (let day in data[year][month]) {
            const numEntries = data[year][month][day].length;
            numColors = Math.max(numColors, numEntries);
          }
        }
      }
    });
</script>

<nav class="bg-cyan-800">
  <div class="px-2 mx-auto max-w-7xl sm:px-6 lg:px-8">
    <div class="flex items-center h-12">
      <div class="py-2 text-2xl font-medium text-white">
        Cabanas WiFi Monitor
      </div>
    </div>
  </div>
</nav>

<main class="px-2 mx-auto mb-4 max-w-7xl sm:px-6 lg:px-8">
  {#each Object.keys(data).sort().reverse() as year}
    <div class="mt-6 text-xl">{year}</div>
    <div class="grid grid-cols-1 gap-4 mt-2 md:grid-cols-2 lg:grid-cols-3">
      {#each Object.keys(data[year]).sort((a, b) => parseInt(b) - parseInt(a)) as month}
        <Month
          year={parseInt(year)}
          month={parseInt(month)}
          max={numColors}
          data={data[year][month]}
        />
      {/each}
    </div>
  {/each}
</main>
