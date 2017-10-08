import React from 'react';
import { AppRegistry, Platform, StatusBar, StyleSheet, Text, ScrollView, Button, View } from 'react-native';
import { AppLoading, Asset, Font } from 'expo';
import { Ionicons } from '@expo/vector-icons';
import RootNavigation from './navigation/RootNavigation';
import { StackNavigator } from 'react-navigation';
import HomeScreen from './screens/HomeScreen.js'
import LinksScreen from './screens/LinksScreen.js'







 class ChatScreen extends React.Component {
  static navigationOptions = {
    title: 'Chat with Lucy',
  };
  render() {
    return (
      <View>
      <Button title="Testing" />
        <Text>Chat with Lucy</Text>
      </View>
    );
  }
}

const SimpleApp= StackNavigator({
  Home: {screen: HomeScreen},
  Chat: {screen: ChatScreen}, 
  Preferences: {screen: LinksScreen}
  
} ,
{swipeEnabled: false, 
animationEnabled: false, }, );



export default class App extends React.Component {
  
  
  state = {
    isLoadingComplete: false,
    
  };


  render() {
    if (!this.state.isLoadingComplete && !this.props.skipLoadingScreen) {
      return (
        <AppLoading
          startAsync={this._loadResourcesAsync}
          onError={this._handleLoadingError}
          onFinish={this._handleFinishLoading}
        />
      );
    } else {
      return (
      
        <ScrollView style={styles.container2}>
          <SimpleApp style={styles.containter}/>
          
        </ScrollView>
      );
    }
  }




  

  _loadResourcesAsync = async () => {
    return Promise.all([
      Asset.loadAsync([
        require('./assets/images/robot-dev.png'),
        require('./assets/images/robot-prod.png'),
      ]),
      Font.loadAsync([
        // This is the font that we are using for our tab bar
        Ionicons.font,
        // We include SpaceMono because we use it in HomeScreen.js. Feel free
        // to remove this if you are not using it in your app
        { 'space-mono': require('./assets/fonts/SpaceMono-Regular.ttf') },
      ]),
    ]);
  };

  _handleLoadingError = error => {
    // In this case, you might want to report the error to your error
    // reporting service, for example Sentry
    console.warn(error);
  };

  _handleFinishLoading = () => {
    this.setState({ isLoadingComplete: true });
  };
}

AppRegistry.registerComponent('SimpleApp', () => SimpleApp);


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  container2: {
    flex: 1,
    backgroundColor: '#fff',
    paddingVertical: 20,
    
  },
  statusBarUnderlay: {
    height: 24,
    backgroundColor: 'rgba(0,0,0,0.2)',
  },
});
