mensagens = {
    "audio": "O destino são dados de áudio. Isso pode ter origem em uma tag HTML <audio>.",
    "audioworklet": "O destino são dados obtidos para uso por um Audio Worklet. Pode ter origem em audioWorklet.addModule().",
    "document": "O destino é um documento (HTML ou XML), normalmente resultado de uma navegação iniciada pelo usuário.",
    "embed": "O destino é conteúdo incorporado por meio de uma tag HTML <embed>.",
    "empty": "Destino sem valor específico. Usado por APIs como fetch(), XMLHttpRequest, WebSocket, EventSource e navigator.sendBeacon().",
    "fencedframe": "O destino é um Fenced Frame.",
    "font": "O destino é uma fonte, geralmente carregada via CSS @font-face.",
    "frame": "O destino é um frame carregado por uma tag HTML <frame>.",
    "iframe": "O destino é um iframe carregado por uma tag HTML <iframe>.",
    "image": "O destino é uma imagem carregada por <img>, SVG <image>, CSS background-image, cursor ou list-style-image.",
    "json": "O destino é um recurso JSON importado como módulo JavaScript.",
    "manifest": "O destino é um manifesto carregado por <link rel='manifest'>.",
    "object": "O destino é um objeto carregado por uma tag HTML <object>.",
    "paintworklet": "O destino é um Paint Worklet carregado por CSS.PaintWorklet.addModule().",
    "report": "O destino é um relatório, como um relatório de Content Security Policy (CSP).",
    "script": "O destino é um script carregado por uma tag <script> ou importScripts().",
    "serviceworker": "O destino é um Service Worker registrado por navigator.serviceWorker.register().",
    "sharedworker": "O destino é um Shared Worker.",
    "style": "O destino é uma folha de estilos carregada por <link rel='stylesheet'> ou CSS @import.",
    "track": "O destino é uma faixa de texto HTML carregada por uma tag <track>.",
    "video": "O destino são dados de vídeo carregados por uma tag HTML <video>.",
    "webidentity": "O destino é um endpoint de verificação de identidade usado pela API FedCM.",
    "worker": "O destino é um Web Worker.",
    "xslt": "O destino é uma transformação XSLT.",
    "desconecido": "O destino é desconhecido ou não especificado."
}

def obter_mensagem_destino_http(destino):
    return mensagens[destino]
