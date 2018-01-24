package extraction;

import edu.stanford.nlp.dcoref.CorefChain;  
import edu.stanford.nlp.dcoref.CorefCoreAnnotations;  
import edu.stanford.nlp.ling.CoreAnnotations;  
import edu.stanford.nlp.ling.CoreLabel;  
import edu.stanford.nlp.pipeline.Annotation;  
import edu.stanford.nlp.pipeline.StanfordCoreNLP;  
import edu.stanford.nlp.semgraph.SemanticGraph;  
import edu.stanford.nlp.semgraph.SemanticGraphCoreAnnotations;  
import edu.stanford.nlp.trees.Tree;  
import edu.stanford.nlp.trees.TreeCoreAnnotations;  
import edu.stanford.nlp.util.CoreMap;  
import edu.stanford.nlp.util.PropertiesUtils;  
import extraction.StanfordEnglishNlpExample;  
  
import java.util.List;  
import java.util.Map;  
import java.util.Properties; 

public class StanfordChineseNlpExample {
	public static void main(String[] args) {  
		  
        StanfordChineseNlpExample example = new StanfordChineseNlpExample();  
  
        example.runChineseAnnotators();  
  
    }  
  
    public void runChineseAnnotators(){  
  
        String text = "���ֶ�˵����ʢ�ٽ�����ʵ�Ժ����ľ���Ԯ����"  
                + "����жԿ��ֶٵĽ����������������ֶ���ͳ�ڻ�̸�����꣬���ᶨ��֧�ֺ������Ѿ���Σ����";  
        Annotation document = new Annotation(text);  
        StanfordCoreNLP corenlp = new StanfordCoreNLP("StanfordCoreNLP-chinese.properties");  
        corenlp.annotate(document);  
        parserOutput(document);  
    }  
  
    public void parserOutput(Annotation document){  
        // these are all the sentences in this document  
        // a CoreMap is essentially a Map that uses class objects as keys and has values with custom types  
        List<CoreMap> sentences = document.get(CoreAnnotations.SentencesAnnotation.class);  
  
        for(CoreMap sentence: sentences) {  
            // traversing the words in the current sentence  
            // a CoreLabel is a CoreMap with additional token-specific methods  
            for (CoreLabel token: sentence.get(CoreAnnotations.TokensAnnotation.class)) {  
                // this is the text of the token  
                String word = token.get(CoreAnnotations.TextAnnotation.class);  
                // this is the POS tag of the token  
                String pos = token.get(CoreAnnotations.PartOfSpeechAnnotation.class);  
                // this is the NER label of the token  
                String ne = token.get(CoreAnnotations.NamedEntityTagAnnotation.class);  
  
                System.out.println(word+"\t"+pos+"\t"+ne);  
            }  
  
            // this is the parse tree of the current sentence  
            Tree tree = sentence.get(TreeCoreAnnotations.TreeAnnotation.class);  
            System.out.println("�﷨����");  
            System.out.println(tree.toString());  
  
            // this is the Stanford dependency graph of the current sentence  
            SemanticGraph dependencies = sentence.get(SemanticGraphCoreAnnotations.CollapsedCCProcessedDependenciesAnnotation.class);  
            System.out.println("����䷨��");  
            System.out.println(dependencies.toString());  
        }  
  
        // This is the coreference link graph  
        // Each chain stores a set of mentions that link to each other,  
        // along with a method for getting the most representative mention  
        // Both sentence and token offsets start at 1!  
        Map<Integer, CorefChain> graph =  
                document.get(CorefCoreAnnotations.CorefChainAnnotation.class);  
    }  
}
