import React, { Component } from 'react';
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
  AppRegistry,
} from 'react-native';
import { WebBrowser } from 'expo';
import { SideMenu, ListItem } from 'react-native-elements';
import { MonoText } from '../components/StyledText';
import { MapView, Permissions, Location, Constants }  from 'expo';
import Polyline from '@mapbox/polyline';
import  App  from 'babel-preset-expo';
import { List } from 'react-native-elements';
import { StackNavigator } from 'react-navigation'


  let { height, width } = Dimensions.get('window');
  let size = width;
  

export default class HomeScreen extends React.Component {
  static navigationOptions = {
    title: 'Start',
  }
  constructor() {
    super()
    
    this.state = {
      coords:[],
      topText: "",
      bottomText: "",
      locationResult: '',
      location: {},
      list: [],
      isOpen: false,
      region: {
        latitude:37.87189, 
        longitude:-122.2539, 
        latitudeDelta: 0.0922,
        longitudeDelta: 0.0421,
      },
    
      restaurant_list: global.restaurant_list,
    }
  }
  

  componentDidMount() {
    // find your origin and destination point coordinates and pass it to our method.
    // I am using Bursa,TR -> Istanbul,TR for this example
    this._getLocationAsync();
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
   
   global.restaurantinfo = [{latitude: this.state.locationResult.latitude, longitude: this.state.locationResult.longitude, name: "Current Location", category: "Current Location"}];
 
 };

 _updateLocation = async() => {
  this.setState()
 }

  async getDirections(startLoc, destinationLoc) {
        try {
            let resp = await fetch(`https://maps.googleapis.com/maps/api/directions/json?origin=${ startLoc }&destination=${ destinationLoc }`)
            let respJson = await resp.json();
            let points = Polyline.decode(respJson.routes[0].overview_polyline.points);
            let coordslist = points.map((point) => {
                return  {
                    latitude : point[0],
                    longitude : point[1],
                }
            })
            this.setState({restaurant_list: global.restaurant_list})
            this.setState({coords: coordslist});
            global.coordinates = this.state.coords;
            this.setState({region: {
              latitude: coordslist[coordslist.length -1].latitude,
              longitude: coordslist[coordslist.length -1 ].longitude,
              latitudeDelta: 0.0922,
              longitudeDelta: 0.0421,
            }});
            return coordslist
        } catch(error) {
            alert(error)
            return error
        }
    }

  render() {

    const { navigate } = this.props.navigation;
    
    return (
      <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}}>
      <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}} 
        >

      <MapView 
      style={{height: 0.8*size, width: size}} 
      /*initialRegion={{
          latitude:41.0082, 
          longitude:28.9784, 
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421
        }} */
        region={this.state.region}
        followUserLocation={true}
        >
        {global.restaurantinfo.map(marker => (
        <MapView.Marker
          coordinate= {{latitude: parseFloat(marker.latitude), longitude: parseFloat(marker.longitude)}}
          title = {marker.name}
          description = {marker.category[0]} 
          pinColor={'#d62424'} />
          ))}
        <MapView.Polyline 
            coordinates={this.state.coords}
            strokeWidth={2}
            strokeColor="red"/>
        </MapView>
        
        <TextInput
          style={styles.textInput}
          onChangeText={text => this.setState({ topText: text })}
          value={this.state.topText}
        />

        <TextInput
          style={styles.textInput}
          onChangeText={text => this.setState({ bottomText: text })}
          value={this.state.bottomText}
        />
        <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}}>
        <Button title="Render" onPress={this._getDirections}/>
        </View>
        <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}}>
        
        <Button title="Center on Me" onPress={this._centerOnUser}/>
        </View>
        <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}}>
        <Button
              onPress={() => navigate('Chat')}
              title="Chat with Lucy"
            />
            </View>
          <View style={{flex:1,flexDirection: 'column', paddingVertical: 20}}>
            <Button
              onPress={() => navigate('Preferences')}
              title="Preferences"
              />
              </View>
        </View>
        
            
        <ScrollView
          style={styles.container}
          contentContainerStyle={styles.contentContainer}>
          

          <View style={styles.getStartedContainer}>

            <Text style={styles.getStartedText}>
              Location: {this.state.locationResult}
              Restaurants: {JSON.stringify(global.restaurant_list)}
              ThisOne: {global.opentable_list.items[0].rid}
            </Text>
          </View>
        </ScrollView>
      
      </View>
    );
  }



  _getDirections = async () => {
    try {
            let resp = await fetch(`https://maps.googleapis.com/maps/api/directions/json?origin=${ this.state.topText }&destination=${ this.state.bottomText }`)
            let respJson = await resp.json();

            let points = Polyline.decode(respJson.routes[0].overview_polyline.points);
            let coordslist = points.map((point) => {
                return  {
                    latitude : point[0],
                    longitude : point[1],
                }
            })
            this.setState({coords: coordslist});

            global.coordinates = this.state.coords;
            this.setState({region: {
              latitude: coordslist[coordslist.length -1].latitude,
              longitude: coordslist[coordslist.length -1 ].longitude,
              latitudeDelta: 0.0922,
              longitudeDelta: 0.0421,
            }});
            this.setState({locationResult: this.state.region})
            return coordslist
        } catch(error) {
            alert(error)
            return error
        }
    }

  

  _handleLearnMorePress = () => {
    WebBrowser.openBrowserAsync(
      'https://docs.expo.io/versions/latest/guides/development-mode'
    );
  };

  _handleHelpPress = () => {
    WebBrowser.openBrowserAsync(
      'https://docs.expo.io/versions/latest/guides/up-and-running.html#can-t-see-your-changes'
    );
  };
}

 

  
  
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  developmentModeText: {
    marginBottom: 20,
    color: 'rgba(0,0,0,0.4)',
    fontSize: 14,
    lineHeight: 19,
    textAlign: 'center',
  },
  contentContainer: {
    paddingVertical: 30,
  },
  textInput: {
    height: 40,
    borderWidth: 1,
    borderColor: 'gray',
    width: width,
  },
  welcomeContainer: {
    alignItems: 'center',
    marginTop: 10,
    marginBottom: 20,
  },
  welcomeImage: {
    width: 100,
    height: 80,
    resizeMode: 'contain',
    marginTop: 3,
    marginLeft: -10,
  },
  getStartedContainer: {
    alignItems: 'center',
    marginHorizontal: 50,
  },
  homeScreenFilename: {
    marginVertical: 7,
  },
  codeHighlightText: {
    color: 'rgba(96,100,109, 0.8)',
  },
  codeHighlightContainer: {
    backgroundColor: 'rgba(0,0,0,0.05)',
    borderRadius: 3,
    paddingVertical: 4,
  },
  getStartedText: {
    fontSize: 17,
    color: 'rgba(96,100,109, 1)',
    lineHeight: 24,
    textAlign: 'center',
  },
  tabBarInfoContainer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    ...Platform.select({
      ios: {
        shadowColor: 'black',
        shadowOffset: { height: -3 },
        shadowOpacity: 0.1,
        shadowRadius: 3,
      },
      android: {
        elevation: 20,
      },
    }),
    alignItems: 'center',
    backgroundColor: '#fbfbfb',
    paddingVertical: 20,
  },
  tabBarInfoText: {
    fontSize: 17,
    color: 'rgba(96,100,109, 1)',
    textAlign: 'center',
  },
  navigationFilename: {
    marginTop: 5,
  },
  helpContainer: {
    marginTop: 15,
    alignItems: 'center',
  },
  helpLink: {
    paddingVertical: 15,
  },
  helpLinkText: {
    fontSize: 14,
    color: '#2e78b7',
  },
});


