import './App.css';
import {Header} from './components/header';
import Footer from './components/footer';

function OurText(){
  return <p>This is our text</p>
};

function createAlert() {
  alert("Thanks for clicking me.")
}

function ShowMessage(props){
  if(props.toShow){
    return <h2>My ending Message</h2>
  }
  return <h2>En Ding Ding Värld</h2>
}

function App() {
  return (
    <div className="App">
      <Header info="This is the daily message" myAlert={createAlert}/>
      <p>
        Hello World
      </p>
      <OurText/>
      <OurText/>
      <OurText/>
      <ShowMessage toShow={true}/>
      <Footer signature="Goodbye from Edvin"/>
    </div>
  );
}

export default App;
