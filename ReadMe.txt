################### 2020. June 19 ######################
# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated... (the manuscript in preparation)
# Contact information: jangwoo.lee@eawag.ch or myjackson@naver.com

# The following datasets are required as a starting point
- M17_prodigal.csv : The annotated ARGs using the ORF (open reading frame) predicted by a relevant pipeline (e.g. Prodigal) for the sample M17
- M17_genes.coverage.csv : The average coverage (and the reference length) for all the ORFs (calculated by the following reference: Albertsen et al., 2013) in the sample
- M17_prodigal_Silva.csv : The annotated 16S rRNA genes using Silva as a reference database for the sample M17 using the predicted ORFs (using Prodigal)
- nrp72_16Scopy.csv : The absolute abundance (copies/mL) of 16S rRNA gene quantified by qPCR for all the samples (only M17 data will be subsetted, and used in the following tutorial codes)

# The work-flow is as follows:
0. To search for average coverage and the length of reference sequence from the calculated coverage datafile (M17_genes.coverage.csv) for each ORF (o f which ARG was annotated), and update those information to the main dataframe (M17_prodigal.csv)- related code: 0. updating_coverage_length_orf.py

1. To calculate the number of reads assigned to each ORF, and calculate the reads per kilobase (RPK) - related code: 1. updating_readno_rpk.py

2. To calculate the genes per million (GPM) - related code: 2. updating_gpm.py

3. To calculate RPK for 16S rRNA gene in the sample, and finally calculate the genes per 16S rRNA gene (GP16S) by dividing the RPK for each ARG-annotated ORF by the RPK for 16S rRNA gene - related code: 3.1. updating_rpk_16S_Silva.py & 3.2. updating_rpk_16S_Silva.py

4. To calculate the genes per liter (GPL) by multiplying GP16S for each gene by 16S absolute abundance (copies/L) - related code: 4. updating_GPL.py

# References:
The coverage for each ORF was calculated following the reference:
- Albertsen, M., Hugenholtz, P., Skarshewski, A., Nielsen, K.L., Tyson, G.W. and Nielsen, P.H. (2013) Genome sequences of rare, uncultured bacteria obtained by differential coverage binning of multiple metagenomes. Nature biotechnology 31(6), 533

This codes were written by Jangwoo Lee referring to the following references in terms of concepts on quantitative metagenome metrics:
- Ju, F., Beck, K., Yin, X., Maccagnan, A., McArdell, C.S., Singer, H.P., Johnson, D.R., Zhang, T. and Bürgmann, H. (2019) Wastewater treatment plant resistomes are shaped by bacterial composition, genetic exchange, and upregulated expression in the effluent microbiomes. The ISME journal 13(2), 346-360.
- Li, B. and Dewey, C.N. (2011) RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome. BMC bioinformatics 12(1), 323.
- Katz, Y., Wang, E.T., Airoldi, E.M. and Burge, C.B. (2010) Analysis and design of RNA sequencing experiments for identifying isoform regulation. Nature methods 7(12), 1009.
