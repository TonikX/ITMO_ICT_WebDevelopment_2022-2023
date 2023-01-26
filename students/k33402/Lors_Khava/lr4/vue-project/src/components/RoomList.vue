<template>
  <div :class="room.status" v-if="room.status === '+'">
    <div class="card mb-5"> 
      <div class="card-image">
        <figure class="image is-2by1">
          <div :class="room.type" v-if="room.type === 'single'" >
            <img  src="/single_room.jpg" alt="single room">
          </div>
          <div :class="room.type" v-if="room.type === 'double'" >
            <img  src="/double_room.jpg" alt="double room">
          </div>
          <div :class="room.type" v-if="room.type === 'triple'" >
            <img  src="/triple_room.jpg" alt="triple room">
          </div>
        </figure>
      </div>  
      <div class="card-content">
        <div class="content">
          <p class="title is-5">Number: {{ room.number }}</p>
          <hr>
          <p class="is-success">Type: {{ room.type }}</p>
          <p class="is-success">Price: {{ room.price }}</p>
          <p class="is-success">Phone: {{ room.phone }}</p>
        </div>
      </div>     
    </div>
  </div>
</template>
   
<script>
  export default {
  name: "RoomCard",
  props: {
    room: Object,
  }
  }
</script>
   