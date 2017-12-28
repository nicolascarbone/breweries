
import axios from 'axios';

export default {
  name: 'app-sidebar',
  data: function () {
    return {
      // items: [1, 2, 3, 4]
    }
  },
  computed: {
    // metodos con attributos que no cambian
  },
  mounted () {
    this.getPlaces();
  },
  methods: {
    getPlaces: function() {
      var vm = this;

      var instance = axios.create({
        baseURL: 'http://127.0.0.1:8000/api/',
        timeout: 1000,
        headers: {
        }
      });

      instance
        .get('places/')
        .then(function (response) {
          vm.places = response.data;
        })
        .catch(function (error) {
          vm.answer = 'Error! Could not reach the API. ' + error
        })
    }
  }
}
