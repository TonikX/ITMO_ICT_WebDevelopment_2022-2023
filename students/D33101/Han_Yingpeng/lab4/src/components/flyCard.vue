<template>
    <div>
      <table>
        <thead>
          <tr>
            <th v-for="key in columns" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in tableData" :key="data.id">
            <td v-for="key in columns" :key="key">{{ data[key] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        tableData: [],
        columns: [],
      };
    },
    created() {
      axios.get('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
          this.tableData = response.data;
          this.columns = Object.keys(this.tableData[0]);
        })
        .catch(error => {
          console.log(error);
        });
    },
  };
  </script>
  