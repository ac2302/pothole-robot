import { React, useState, useEffect } from "react";
import "axios";
import "./App.css";
import axios from "axios";

function App() {
	const [piLocation, setPilocation] = useState(null);
	const [state, setState] = useState(null);
	const [command, setCommand] = useState(null);

	useEffect(() => {
		console.log(`http://${piLocation}:5000/state`);
		axios
			.get(`http://${piLocation}:5000/state`)
			.then((res) => {
				console.log(res.data);
				setState(res.data);
			})
			.catch((err) => console.error(err));
	}, [piLocation]);

	useEffect(() => {
		console.log(command);

		axios
			.post(`http://${piLocation}:5000/move`, { command: command })
			.then((res) => console.log(res.data))
			.catch((err) => {
				console.error(err);
			});
	}, [command]);

	document.addEventListener("keydown", (e) => {
		if (e.key == "ArrowUp" && command != "straight") {
			setCommand("straight");
		} else if (e.key == "ArrowLeft" && command != "left") {
			setCommand("left");
		} else if (e.key == "ArrowRight" && command != "right") {
			setCommand("right");
		} else if (e.key == "ArrowDown" && command != "right") {
			setCommand("stop");
		}
	});
	document.addEventListener("keyup", (e) => {
		setCommand("auto");
	});

	return (
		<div>
			{piLocation ? (
				<>
					<img src={`http://${piLocation}:5000/video`} />
					<h4>controls</h4>
					<ul>
						<li>hold left arrow key: go left</li>
						<li>hold right arrow key: go right</li>
						<li>hold up arrow key: go straight</li>
						<li>hold down arrow key: halt</li>
					</ul>
				</>
			) : (
				<>
					<input id="pilocation" />
					<button
						onClick={() => {
							setPilocation(document.getElementById("pilocation").value);
						}}
					>
						set location
					</button>
				</>
			)}
		</div>
	);
}

export default App;
