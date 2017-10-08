import React from 'react';
import './global.js';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  Dimensions,
  TextInput,
  Button,
} from 'react-native';
import { MapView, Permissions, Location, Constants } from 'expo';
import { WebBrowser } from 'expo';
import { SideMenu, ListItem } from 'react-native-elements';
import { MonoText } from '../components/StyledText';
import Polyline from '@mapbox/polyline';
import  App  from 'expo';
import { List } from 'react-native-elements';
import { ExpoLinksView } from '@expo/samples';
import { StackNavigator } from 'react-navigation'


export default class LinksScreen extends React.Component {
  static navigationOptions = {
    title: 'Preferences',
  };
  constructor() {
    super();

  this.state = {
    locationResult: '',
    restaurant_list: [],
    maximumdist: 0.3,
    isOpen: false,
    list: [({subtitle: "Testing", subtitle: "Justin Bui"}, "mykey")],
  }
}

componentDidMount() {
  this._getLocationAsync();
  alert("Are we executing linkscreen");
  this.forceUpdate();
}

  _getLocationAsync = async () => {
   let { status } = await Permissions.askAsync(Permissions.LOCATION);
   if (status !== 'granted') {
     this.setState({
       locationResult: 'Permission to access location was denied',
     });
   }

   let location = await Location.getCurrentPositionAsync({});
   this.setState({ locationResult: JSON.stringify(location) });
   this.setState({location: location});
   global.currentloc = this.state.locationResult;
   global.restaurantinfo = [{latitude: this.state.locationResult.latitude, longitude: this.state.locationResult.longitude, name: "Current Location", category: "Current Location"}];
 };

  render() {
    alert("Render this")
    const { navigate } = this.props.navigation;

    return (

      <View style={styles.container}>
        
        <Button title="Find Me Something On My Way!" onPress={this._filterRestaurants} />
        <Text style={styles.getStarted}>
            Restaurants:{JSON.stringify(this.state.restaurant_list)}

        </Text>
      </View>
    );
  }

    


  _getRestaurants = async () => {
    try{
        var coords = this.state.location.coords;
        coords = JSON.stringify(coords.latitude) + "," + JSON.stringify(coords.longitude)
      let resp = await fetch(`https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${ coords }&rankby=distance&type=restaurant&key=AIzaSyDJdwmhCdXJkfzXfqjFN4BA-aCb3p87K5c`)
      let respJson = await resp.json();
      var restaurant_list = []
      for (var i=0; i<respJson.results.length; i++) {
          restaurant_list.push(respJson.results[i].name);
      }
      this.setState({restaurant_list: restaurant_list})
      global.restaurant_list = this.state.restaurant_list
      alert(JSON.stringify(restaurant_list));
    } catch(error) {
      alert(error)
      return error
    }
  }

  _filterRestaurants = async() => {
    try {
      var uniqueRestaurants = [];
      var uniquenames = [];
      var operatethis = global.coordinates;
      var restaurantholder = global.opentable_list.items;
      for (var i = 0 ; i < operatethis.length; i++) {
        for (var j = 0; j < restaurantholder.length; j++) {
            var eucdistlat = operatethis[i].latitude - restaurantholder[j].latitude;
            var eucdistlong = operatethis[i].longitude - restaurantholder[j].longitude;
            var eucdist = Math.sqrt((eucdistlat * eucdistlat) + (eucdistlong * eucdistlong));
            if ( eucdist <= this.state.maximumdist && !uniqueRestaurants.includes(restaurantholder[j])) {
              uniqueRestaurants.push(restaurantholder[j]);
              uniquenames.push(restaurantholder[j].name);
            }
        }
      }
      this.setState({restaurant_list: uniquenames});
      global.restaurant_list = this.state.restaurant_list;
      global.restaurantinfo = uniqueRestaurants;

      } catch(error) {
        alert(error);
      }
    }
  }


const styles = StyleSheet.create({
  container: {
    
    paddingTop: 15,
    paddingBottom: 15,
    backgroundColor: '#fff',
  },
  getStarted: {
      fontSize: 17,
      color: 'rgba(96,100,1009,1)',
      lineHeight: 24,
        textAlign: 'center',
  }
});
