function showComposerSheetMusic() {
    // Создание AJAX-запроса
    var xhr = new XMLHttpRequest();
    
    // Установка URL-адреса и метода запроса
    xhr.open('GET', '', true);
    
    // Установка обработчика события загрузки
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Обработка ответа от сервера
        var sheetMusicDiv = document.getElementById('sheet-music');
        sheetMusicDiv.innerHTML = xhr.responseText;
      }
    };
    
    // Отправка запроса
    xhr.send();
  }