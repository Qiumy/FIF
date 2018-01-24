package extraction;

import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.simple.*;

/**
 * A demo illustrating how to call the OpenIE system programmatically.
 */
public class OpenIEDemo2 {

  public static void main(String[] args) throws Exception {
    // Create a CoreNLP document
    Document doc = new Document("Obama was born in Hawaii. He is our president.");

    // Iterate over the sentences in the document
    for (Sentence sent : doc.sentences()) {
      // Iterate over the triples in the sentence
      for (RelationTriple triple : sent.openieTriples()) {
        // Print the triple
        System.out.println(triple.confidence + "\t" +
            triple.subjectLemmaGloss() + "\t" +
            triple.relationLemmaGloss() + "\t" +
            triple.objectLemmaGloss());
      }
    }
  }
}