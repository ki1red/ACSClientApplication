const { app, BrowserWindow } = require('electron');
const fluent_ffmpeg = require('fluent-ffmpeg');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    frame: false, // Убираем рамки окна
    fullscreen: false, // Запускаем в полноэкранном режиме
    webPreferences: {
      nodeIntegration: true
    }
  });

  // Загрузка статичной картинки по умолчанию
  mainWindow.loadFile('default.jpg');

  // Отключаем меню окна
  mainWindow.setMenu(null);

  // Подключение к трансляции RTMP
  const rtmpUrl = 'rtmp://localhost:1935/live/stream'; // Ваш URL для трансляции RTMP
  ffmpeg.setFfmpegPath('C:\\ffmpeg\\bin\\ffmpeg.exe');
  fluent_ffmpeg()
    .input(rtmpUrl)
    .outputOptions('-c:v copy')
    .outputOptions('-c:a aac')
    .outputOptions('-strict experimental')
    .outputOptions('-bufsize 512k')
    .outputOptions('-f flv')
    .outputOptions('-max_muxing_queue_size 1024')
    .on('start', () => {
      console.log('FFmpeg started');
    })
    .on('error', (err, stdout, stderr) => {
      console.error('FFmpeg error:', err.message);
      console.error('FFmpeg stderr:', stderr);
    })
    .on('end', () => {
      console.log('FFmpeg ended');
    })
    .pipe(mainWindow, { end: true });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
