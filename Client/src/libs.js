export function dummyPy() {
  return new window.PythonShell("lib/dummy.py");
}

export function readCardPy() {
  return new window.PythonShell("lib/access_card.py");
}

export function ReadCard() {
  this.shell = readCardPy()

  const handleMessage = (resolve, reject) => {
    const handle = (message) => {
      const [command, payload] = message.split(",");
      if (command === "status" && payload === "scanning") {
        this.scanning = true;
      } else if (command === "result") {
        this.shell.removeListener('message', handle)
        this.scanning = false;
        resolve(payload);
      } else {
        this.shell.removeListener('message', handle)
        reject("unexpected message");
      }

    }
    return handle;
  }

  this.scanning = false;
  this.read = () => new Promise((resolve, reject) => {
    this.shell.on('message', handleMessage(resolve, reject));
    this.shell.send("start");
  });

  this.stop = () => this.shell.end((err, code, signal) => new Promise((resolve, reject) => {
    this.shell = readCardPy();
    if (err) reject(err);
    resolve(true);
  }));
}