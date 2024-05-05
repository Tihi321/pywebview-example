import { createSignal } from 'solid-js'
import solidLogo from './assets/solid.svg'
import viteLogo from '/vite.svg'
import './App.css'

const getPyWebview = () => window?.pywebview?.api || {send: async () => "No pywebview"};

const sendMessage = async (value) => {
  const message = await getPyWebview().send(value);

  return message;
};

function App() {
  const [messages, setMessages] = createSignal([]);

  const onChange = (e) => {
    const mesage = e.target.value;
    sendMessage(mesage).then((value) => {
      setMessages((prev) => [...prev, value]);
    });
    e.target.value = '';
  };

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} class="logo" alt="Vite logo" />
        </a>
        <a href="https://solidjs.com" target="_blank">
          <img src={solidLogo} class="logo solid" alt="Solid logo" />
        </a>
      </div>
      <h1>Vite + Solid</h1>
      <input type="text" onChange={onChange}/>
      <div class="card">
        <h2>Messages</h2>
        <ul>
          {messages().map((message) => (
            <li>{message}</li>
          ))}
        </ul>
      </div>
    </>
  )
}

export default App
