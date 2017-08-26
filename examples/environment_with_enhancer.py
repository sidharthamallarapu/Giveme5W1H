from util import StartupHelper


def start():
    h = StartupHelper()
    h.do_command('CoreNLP','java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000', 'stanford-corenlp-full-2016-10-31')
    h.do_command('AIDA','mvn jetty:run -Djetty.http.port=9001', 'aida-3.0.4')
    h.forever()
start()