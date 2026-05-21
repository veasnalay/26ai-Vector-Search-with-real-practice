# 26ai-Vector-Search-with-real-practice
Oracle AI Vector Search in Oracle Database 26ai is Oracle's built-in vector database capability that allows you to perform semantic similarity searches directly inside the database without requiring a separate vector store such as Pinecone, Milvus, or Weaviate. It is a core feature of Oracle AI Database 26ai
*** Noted Make sure you are using oracle 26ai

1 )- Verify embedding tool 
    # python3.9 -m pip list | grep sentence
  	  sentence-transformers    5.1.2

      ** noted : the compatible python version with sentence transformers
          python3.9 required : ImportError: huggingface-hub>=0.34.0,<1.0 is required

     -- install the required version 
       pip3.9 install --upgrade --force-reinstall \
		    sentence-transformers \
		    transformers \
		    "huggingface-hub<1.0"

    -- Verify compatible version 

      $ python3.9 -c "import sentence_transformers; print('OK')"
			OK

2 )- Test model 

    $ python3.9 test_vector.py

    ** result  should be 384


3 )- Embedding table Employees from 

    ** query Text Data from existing table (Employees Table) 
	
	
		$ sqlplus 'hr/"hr"@PDB23AI'
		
		
		SELECT employee_id,
		first_name || ' ' || last_name || ', ' ||
		job_id || ', salary ' || salary || ', dept ' || department_id AS text_data
		FROM hr.employees;


    -- output :

      *EMPLOYEE_ID TEXT_DATA
		*----------- ---------------------------------------------------------------------------------------------
		*		111 Ismael Sciarra, FI_ACCOUNT, salary 7700, dept 100
		*		112 Jose Manuel Urman, FI_ACCOUNT, salary 7800, dept 100
		*		113 Luis Popp, FI_ACCOUNT, salary 6900, dept 100
		*		115 Alexander Khoo, PU_CLERK, salary 3100, dept 30
		*		100 Steven King, AD_PRES, salary 24000, dept 90
		*		101 Neena Yang, AD_VP, salary 17000, dept 90
		*		102 Lex Garcia, AD_VP, salary 17000, dept 90
		*		103 Alexander James, IT_PROG, salary 9000, dept 60
		*		104 Bruce Miller, IT_PROG, salary 6000, dept 60
		*		105 David Williams, IT_PROG, salary 4800, dept 60
		*		106 Valli Jackson, IT_PROG, salary 4800, dept 60

4 )- Add new column to Employees table ( embedding ) with vector model 

	  ALTER TABLE hr.employees ADD (embedding VECTOR(384));

5 )- import Embedding value to embedding column 

    $ python3.9 load_embedding.py
		✅ Embeddings stored successfully


      -- output :

        *SQL> select embedding from employees;
			*
			*	EMBEDDING
			*	------------------------------------------------------------------------------------------------------
			*	[1.08022199E-004,2.9416889E-002,-1.5820168E-002,5.63335679E-002,
			*	[-3.49623635E-002,1.84797272E-002,3.77410441E-003,2.33584605E-002,
			*	[-3.94028351E-002,7.16735516E-003,-3.82486009E-003,1.32008363E-002,
			*	[-9.34902951E-002,5.31440824E-002,-8.40770826E-002,-2.02658381E-002,
			*	[-9.81421843E-002,1.07365549E-002,-1.02997143E-002,5.79342209E-002,
			*	[-9.89049003E-002,-1.73640139E-002,-3.45469895E-003,5.56489527E-002,
			*	[-7.29519725E-002,-1.91987175E-002,-2.15768069E-002,2.52144388E-003,
			*	[-1.00215144E-001,5.50224036E-002,-1.48491347E-002,-4.42040525E-002,
			*	[-4.29749228E-002,-4.67892084E-003,-9.75647569E-002,3.18254866E-002,
			*	[-3.66621949E-002,8.04703161E-002,-6.5031196E-003,3.49506736E-002,
			*	[-9.08539966E-002,1.87588222E-002,-2.66703293E-002,4.16907854E-002,

6) - Test Search result
     
      -- search the word : "programer"
     
       $ python3.9 search_result.py
  			Search Employees :  programer   >>>>>>>>>>>>>>>>>>>>>>>>>> input value
  			(103, 'Alexander', 'James')
  			(117, 'Sigal', 'Tobias')
  			(104, 'Bruce', 'Miller')
  			(183, 'Girard', 'Geoni')
  			(168, 'Lisa', 'Ozer')


      -- search the word : "finance"
     
        $ python3.9 search_result.py
  			Search Employees :  finance   >>>>>>>>>>>>>>>>>>>>>>>>>>>> Input Value
  			(111, 'Ismael', 'Sciarra')
  			(109, 'Daniel', 'Faviet')
  			(122, 'Payam', 'Kaufling')
  			(121, 'Adam', 'Fripp')
  			(170, 'Tayler', 'Fox')
      
