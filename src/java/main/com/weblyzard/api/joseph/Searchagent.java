package com.weblyzard.api.joseph;

import java.io.Serializable;
import java.util.List;

import javax.xml.bind.annotation.XmlRootElement;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * 
 * @author philipp.kuntschik@htwchur.ch
 *
 */
@JsonIgnoreProperties(ignoreUnknown = true)
@XmlRootElement
public class Searchagent implements Serializable  {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public String name;
	public int id;
	public List<Product> product_list;



	public Searchagent setProduct_list(List<Product> product_list) {
		this.product_list = product_list;
		return this;
	}



	public Searchagent setName(String name) {
		this.name = name;
		return this;
	}



	public Searchagent setId(int id) {
		this.id = id;
		return this;
	}

}
