<script lang="ts">
  import Month from "./lib/Month.svelte";
  let data: Object = {};
  let numColors = 0;
  let lastUpdated = "";

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

  fetch("https://api.github.com/repos/sonovice/cabanas/commits?per_page=1")
    .then((response) => response.json())
    .then((response) => {
      const date = response[0].commit.author.date;
      lastUpdated = date.substring(0, 10) + " @ " + date.substring(11, 16);
    });
</script>

<nav class="text-white bg-teal-800">
  <div class="px-2 mx-auto max-w-7xl sm:px-6 lg:px-8">
    <div class="items-center justify-between min-h-8 md:flex">
      <div class="text-2xl font-medium uppercase">
        Cabanas WiFi Monitor
      </div>
      <div class="py-2 text-sm">
        Last updated: {lastUpdated}
      </div>
    </div>
  </div>
</nav>

<main class="px-2 mx-auto mb-4 max-w-7xl sm:px-6 lg:px-8">
  {#each Object.keys(data).sort().reverse() as year}
    <div class="mt-8 text-2xl">{year}</div>
    <div class="grid grid-cols-1 gap-6 mt-2 mb-12 md:grid-cols-2 lg:grid-cols-3">
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
