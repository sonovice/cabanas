<script lang="ts">
  // import logo from "./assets/svelte.png";
  // import Counter from "./lib/Counter.svelte";
  import Month from "./lib/Month.svelte";

  const data: object = {
    2021: {
      9: {
        3: ["MAC1", "MAC2"],
        21: ["MAC17"],
      },
      3: {
        1: [""],
        2: ["", ""],
        3: ["", "", ""],
        4: ["", "", "", ""],
        5: ["", "", "", "", ""],
        6: ["", "", "", "", "", ""],
        7: ["", "", "", "", "", "", ""],
        8: ["", "", "", "", "", "", "", ""],
        9: ["", "", "", "", "", "", "", "", ""],
        10: ["", "", "", "", "", "", "", "", "", ""],
        29: ["", "", "", "", ""],
      },
    },
    2020: {
      1: {
        3: ["Foo"],
      },
    },
  };

  let numColors = 0;
  for (let year in data) {
    for (let month in data[year]) {
      for (let day in data[year][month]) {
        const numEntries = data[year][month][day].length;
        numColors = Math.max(numColors, numEntries);
      }
    }
  }
</script>

<!-- <img src={logo} alt="Svelte Logo" /> -->

<nav class="bg-cyan-800">
  <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
    <div class="flex items-center h-12">
      <div class="text-white text-2xl font-medium py-2">
        Cabanas WiFi Monitor
      </div>
    </div>
  </div>
</nav>

<main class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8 mb-4">
  {#each Object.keys(data).sort().reverse() as year}
    <div class="text-xl mt-6">{year}</div>
    <div class="mt-2 grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
      {#each Object.keys(data[year]).sort().reverse() as month}
        <Month {year} {month} max={numColors} data={data[year][month]} />
      {/each}
    </div>
  {/each}
</main>
