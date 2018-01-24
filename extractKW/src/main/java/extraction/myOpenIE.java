package extraction;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Properties;

import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.naturalli.NaturalLogicAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;
import edu.stanford.nlp.util.PropertiesUtils;

import util.jdbcUtils;

public class myOpenIE {
	private myOpenIE() {
	} // static main
	
	/**
	 * Information Extraction
	 * @param args
	 * @return 
	 * @throws Exception
	 */
	public static ArrayList<String> getExtraction(String text) throws Exception {
		Properties props = PropertiesUtils.asProperties("annotators",
				"tokenize,ssplit,pos,lemma,depparse,natlog,openie");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
		
		Annotation doc = new Annotation(text);
		pipeline.annotate(doc);

		// Loop over sentences in the document
		ArrayList<String> extraction = new ArrayList<String>();
//		int sentNo = 0;
		for (CoreMap sentence : doc.get(CoreAnnotations.SentencesAnnotation.class)) {
//			System.out.println("Sentence #" + ++sentNo + ": " + sentence.get(CoreAnnotations.TextAnnotation.class));

			// Get the OpenIE triples for the sentence
			Collection<RelationTriple> triples = sentence.get(NaturalLogicAnnotations.RelationTriplesAnnotation.class);

			// Print the triples
			for (RelationTriple triple : triples) {
				System.out.println(triple.confidence + "\t" + triple.subjectLemmaGloss() + "\t"
						+ triple.relationLemmaGloss() + "\t" + triple.objectLemmaGloss());
				
				if(triple.subjectLemmaGloss().isEmpty())
					extraction.add(null);
				else
					extraction.add(triple.subjectLemmaGloss());
				if(triple.relationLemmaGloss().isEmpty())
					extraction.add(null);
				else
					extraction.add(triple.relationLemmaGloss());
				if(triple.objectLemmaGloss().isEmpty())
					extraction.add(null);
				else
					extraction.add(triple.objectLemmaGloss());
				break;
			}
		}
		return extraction;	
	}

	public static void main(String[] args) throws Exception {
		// Create the Stanford CoreNLP pipeline
		Properties props = PropertiesUtils.asProperties("annotators",
				"tokenize,ssplit,pos,lemma,depparse,natlog,openie");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

		// Annotate an example document.
		String text;
		if (args.length > 0) {
			text = IOUtils.slurpFile(args[0]);
		} else {
			// text = "Obama was born in Hawaii. He is our president.";
			text = "Baidu shares slip on forecast";
		}
		Annotation doc = new Annotation(text);
		pipeline.annotate(doc);

		// Loop over sentences in the document
		int sentNo = 0;
		for (CoreMap sentence : doc.get(CoreAnnotations.SentencesAnnotation.class)) {
			System.out.println("Sentence #" + ++sentNo + ": " + sentence.get(CoreAnnotations.TextAnnotation.class));

			// Get the OpenIE triples for the sentence
			Collection<RelationTriple> triples = sentence.get(NaturalLogicAnnotations.RelationTriplesAnnotation.class);

			// Print the triples
			for (RelationTriple triple : triples) {
				System.out.println(triple.confidence + ":\t" + triple.subjectLemmaGloss() + ":\t"
						+ triple.relationLemmaGloss() + ":\t" + triple.objectLemmaGloss());
			}

		}
		
		
	}
}
