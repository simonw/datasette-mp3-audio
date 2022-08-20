document.addEventListener("DOMContentLoaded", () => {
  let currentlyPlaying = null;
  function playAllAudios() {
    let audios = Array.from(document.querySelectorAll('audio'));
    function playNext() {
        if (!audios.length) {
            return;
        }
        currentlyPlaying = audios.shift();
        let listener = () => { playNext(); }
        currentlyPlaying.endedListener = listener;
        currentlyPlaying.addEventListener('ended', listener);
        currentlyPlaying.play();
    }
    playNext();
  }

  const audios = document.querySelectorAll('audio');
  if (audios.length < 2) {
    // Not enough audio elements
    return;
  }
  // Add a button to play all
  const button = document.createElement('button');
  button.setAttribute('type', 'button');
  // Datasette button CSS looks for form button[type=button]
  const form = document.createElement('form');
  form.style.marginBottom = '1em';
  form.appendChild(button);
  button.innerText = `Play ${audios.length} MP3s on this page`;
  let isPlaying = false;
  button.addEventListener('click', () => {
    if (!isPlaying) {
      // First clean up any previous endedListener
      audios.forEach(el => {
        el.currentTime = 0;
        if (el.endedListener) {
          el.removeEventListener('ended', el.endedListener);
        }
      });
      playAllAudios();
      isPlaying = true;
      button.innerText = `Playing all ${audios.length} MP3s - Stop`;
    } else {
      if (currentlyPlaying) {
        currentlyPlaying.pause();
      }
      isPlaying = false;
      button.innerText = `Play ${audios.length} MP3s on this page`;
    }
  });
  const tableWrapper = document.querySelector('.table-wrapper');
  tableWrapper.parentNode.insertBefore(form, tableWrapper);
});
